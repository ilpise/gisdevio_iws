/*
 * Copyright 2021, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
*/

import { head, isString } from 'lodash';
import moment from 'moment';
import assign from 'object-assign';
import React , { useEffect } from 'react';
import { Glyphicon } from 'react-bootstrap';
import { connect } from 'react-redux';
import {
    branch,
    compose,
    defaultProps,
    renderNothing,
    setDisplayName,
    withProps,
    withState,
    withStateHandlers
} from 'recompose';
import { createSelector } from 'reselect';

/* Actions */
import { setCurrentOffset } from '@mapstore/framework/actions/dimension'; 
import { selectPlaybackRange } from '@mapstore/framework/actions/playback';
import { enableOffset, onRangeChanged, selectTime, setMapSync, initTimeline } from '@mapstore/framework/actions/timeline';
/* Components */
import Message from '@mapstore/framework/components/I18N/Message';
import tooltip from '@mapstore/framework/components/misc/enhancers/tooltip';
import withResizeSpy from '@mapstore/framework/components/misc/enhancers/withResizeSpy';
import Toolbar from '@mapstore/framework/components/misc/toolbar/Toolbar';
import InlineDateTimeSelector from '@mapstore/framework/components/time/InlineDateTimeSelector';
/* Selectors */
import { currentTimeSelector, offsetEnabledSelector } from '@mapstore/framework/selectors/dimension';
import { mapLayoutValuesSelector } from '@mapstore/framework/selectors/maplayout';
import { playbackRangeSelector, statusSelector } from '@mapstore/framework/selectors/playback';
import {
    currentTimeRangeSelector,
    isMapSync,
    isVisible,
    rangeSelector,
    timelineLayersSelector
} from '@mapstore/framework/selectors/timeline';

/* ?? Customization ?? */
// import Timeline from './timeline/Timeline';
// import TimelineToggle from './timeline/TimelineToggle';

// Get the Timeline and TimelineToggle from compiled mapstore
import Timeline from '@mapstore/framework/plugins/timeline/Timeline';
import Timelinetoggle from '@mapstore/framework/plugins/timeline/TimelineToggle';

/** Components */
import ButtonRB from '@mapstore/framework/components/misc/Button';
import { isTimelineVisible } from "@mapstore/framework/utils/LayersUtils";
import Loader from '@mapstore/framework/components/misc/Loader';

const Button = tooltip(ButtonRB);


const isPercent = (val) => isString(val) && val.indexOf("%") !== -1;
const getPercent = (val) => parseInt(val, 10) / 100;
const isValidOffset = (start, end) => moment(end).diff(start) > 0;













const ExtensionPlugin = compose(
    connect(
        createSelector(
            isVisible,
            timelineLayersSelector,
            currentTimeSelector,
            currentTimeRangeSelector,
            offsetEnabledSelector,
            playbackRangeSelector,
            statusSelector,
            rangeSelector,
            (state) => state.timeline?.loader !== undefined,
            (visible, layers, currentTime, currentTimeRange, offsetEnabled, playbackRange, status, viewRange, timelineIsReady) => ({
                visible,
                layers,
                currentTime,
                currentTimeRange,
                offsetEnabled,
                playbackRange,
                status,
                viewRange,
                timelineIsReady
            })
        ), {
            setCurrentTime: selectTime,
            onOffsetEnabled: enableOffset,
            setOffset: setCurrentOffset,
            setPlaybackRange: selectPlaybackRange,
            moveRangeTo: onRangeChanged,
            onInit: initTimeline
        }),
    branch(({ visible = true, layers = [] }) => !visible || Object.keys(layers).length === 0, renderNothing),

    withState('options', 'setOptions', ({expandedPanel}) => {
        return { collapsed: !expandedPanel };
    }),
    // add mapSync button handler and value
    connect(
        createSelector(isMapSync, mapSync => ({mapSync})),
        {
            toggleMapSync: setMapSync
        }
    ),
    //
    // ** Responsiveness to container.
    // These enhancers allow to properly place the timeline inside the map
    // and resize it or hide accordingly with the available space
    //
    compose(
        // get container size
        compose(
            withStateHandlers(() => ({}), {
                onResize: () => ({ width }) => ({ containerWidth: width })
            }),
            withResizeSpy({ querySelector: ".ms2", closest: true, debounceTime: 100 })
        ),
        defaultProps({
            showHiddenLayers: false,
            expandLimit: 20,
            snapType: "start",
            endValuesSupport: undefined,
            style: {
                marginBottom: 35,
                marginLeft: 100,
                marginRight: 80
            }
        }),
        // get info about expand, collapse panel
        connect( createSelector(
            state => mapLayoutValuesSelector(state, { right: true, bottom: true, left: true }),
            mapLayoutStyle => ({mapLayoutStyle}))),
        // guess when to hide
        withProps(
            ({containerWidth, style, mapLayoutStyle}) => {
                const { marginLeft, marginRight} = style || {};
                let {left = 0, right = 0} = mapLayoutStyle;
                right = isPercent(right) && (getPercent(right) * containerWidth) || right;
                left = isPercent(left) && (getPercent(left) * containerWidth) || left;

                const minWidth = 410;

                if (containerWidth) {
                    const availableWidth = containerWidth - right - left - marginLeft - marginRight;
                    return {
                        hide: availableWidth < minWidth,
                        compactToolbar: availableWidth < 880,
                        style: {...style, ...mapLayoutStyle, minWidth}
                    };
                }
                return {style: {...style, ...mapLayoutStyle, minWidth}};
            }
        ),
        // effective hide
        branch(({ hide }) => hide, renderNothing),
        setDisplayName("TimelinePlugin")
    )
)(  // EXTENSION
    ({
        items,
        options,
        setOptions,
        mapSync,
        toggleMapSync = () => {},
        currentTime,
        setCurrentTime,
        offsetEnabled,
        onOffsetEnabled,
        currentTimeRange,
        setOffset,
        style,
        status,
        viewRange,
        moveRangeTo,
        compactToolbar,
        showHiddenLayers,
        expandLimit,
        snapType,
        endValuesSupport,
        onInit = () => {},
        layers,
        timelineIsReady
    }) => {
        useEffect(()=>{
            // update state with configs coming from configuration file like localConfig.json so that can be used as props initializer
            onInit(showHiddenLayers, expandLimit, snapType, endValuesSupport);
        }, [onInit]);

        const { hideLayersName, collapsed } = options;

        const playbackItem = head(items && items.filter(item => item.name === 'playback'));
        const Playback = playbackItem && playbackItem.plugin;

        const zoomToCurrent = (time, type, view, offsetRange ) => {
            const shift = moment(view.end).diff(view.start) / 2;
            if (type === "time-current" && view) {
                // if the current time is centered to viewRange do nothing
                view.start.toString() !== moment(time).add(-1 * shift).toString() && view.end.toString() !== moment(time).add(shift).toString()
                && moveRangeTo({
                    start: moment(time).add(-1 * shift),
                    end: moment(time).add(shift)
                });
            }
            // center to the current offset range
            if (type === "range-start" || type === "range-end") {
                const offsetRangeDistance = moment(offsetRange.end).diff(offsetRange.start);
                const offsetCenter = moment(offsetRange.start).add(offsetRangeDistance / 2);
                // if the range is smaller than the view range then move the range
                if ( offsetRangeDistance / 2 <= shift ) {
                    moveRangeTo({
                        start: moment(offsetCenter).add(-1 * shift),
                        end: moment(offsetCenter).add(shift)
                    });
                // if offset range is wider than the view range zoom out + move
                } else {
                    moveRangeTo({
                        start: moment(offsetCenter).add(-1 * offsetRangeDistance * 5 / 2),
                        end: moment(offsetCenter).add( offsetRangeDistance * 5 / 2)
                    });
                }
            }
        };

        return (<div
            style={{
                position: "absolute",
                marginBottom: 35,
                marginLeft: 100,
                ...style,
                right: collapsed ? 'auto' : (style.right || 0)
            }}
            className={`timeline-plugin${hideLayersName ? ' hide-layers-name' : ''}${offsetEnabled ? ' with-time-offset' : ''} ${!isTimelineVisible(layers) ? 'hidden' : ''}`}>

            {offsetEnabled // if range is present and configured, show the floating start point.
                && <InlineDateTimeSelector
                    clickable={!collapsed}
                    glyph="range-start"
                    onIconClick= {(time, type) => status !== "PLAY" && zoomToCurrent(time, type, viewRange, currentTimeRange)}
                    tooltip={<Message msgId="timeline.rangeStart"/>}
                    showButtons
                    date={currentTime || currentTimeRange && currentTimeRange.start}
                    onUpdate={start => (currentTimeRange && isValidOffset(start, currentTimeRange.end) || !currentTimeRange) && status !== "PLAY" && setCurrentTime(start)}
                    className="shadow-soft"
                    style={{
                        position: 'absolute',
                        top: -5,
                        left: 2,
                        transform: 'translateY(-100%)'
                    }} />}

            <div
                className={`thredds timeline-plugin-toolbar${compactToolbar ? ' ms-collapsed' : ''}`}>
                {offsetEnabled && currentTimeRange
                    // if range enabled, show time end in the timeline
                    ? <InlineDateTimeSelector
                        clickable={!collapsed}
                        glyph={'range-end'}
                        onIconClick= {(time, type) => status !== "PLAY" && zoomToCurrent(time, type, viewRange, currentTimeRange)}
                        tooltip={<Message msgId="timeline.rangeEnd"/>}
                        date={currentTimeRange.end}
                        showButtons
                        onUpdate={end => status !== "PLAY" && isValidOffset(currentTime, end) && setOffset(end)} />
                    : // show current time if using single time
                    <InlineDateTimeSelector
                        clickable={!collapsed}
                        glyph={'time-current'}
                        showButtons
                        onIconClick= {(time, type) => status !== "PLAY" && zoomToCurrent(time, type, viewRange)}
                        tooltip={<Message msgId="timeline.currentTime"/>}
                        date={currentTime || currentTimeRange && currentTimeRange.start}
                        onUpdate={start => (currentTimeRange && isValidOffset(start, currentTimeRange.end) || !currentTimeRange) && status !== "PLAY" && setCurrentTime(start)} />}
                <div className="timeline-plugin-btn-group">
                    <Toolbar
                        btnDefaultProps={{
                            className: 'square-button-md',
                            bsStyle: 'primary'
                        }}
                        buttons={[
                            {
                                glyph: 'list',
                                tooltip: <Message msgId={!hideLayersName ? "timeline.hideLayerName" : "timeline.showLayerName" } />,
                                bsStyle: !hideLayersName ? 'success' : 'primary',
                                visible: !collapsed,
                                active: !hideLayersName,
                                onClick: () => setOptions({ ...options, hideLayersName: !hideLayersName })
                            },
                            {
                                glyph: 'time-offset',
                                bsStyle: offsetEnabled ? 'success' : 'primary',
                                active: offsetEnabled,
                                disabled: status === "PLAY",
                                tooltip: <Message msgId={!offsetEnabled ? "timeline.enableRange" : "timeline.disableRange"} />,
                                onClick: () => {
                                    if (status !== "PLAY") onOffsetEnabled(!offsetEnabled);

                                }
                            },
                            {
                                glyph: "map-synch",
                                tooltip: <Message msgId={mapSync ? "timeline.mapSyncOn" : "timeline.mapSyncOff"} />,
                                bsStyle: mapSync ? 'success' : 'primary',
                                active: mapSync,
                                onClick: () => toggleMapSync(!mapSync)

                            }
                        ]} />
                    {Playback && <Playback
                        {...playbackItem}
                        settingsStyle={{
                            right: (collapsed || compactToolbar) ? 40 : 'unset'
                        }}/>}
                </div>

                <Button
                    onClick={() => setOptions({ ...options, collapsed: !collapsed })}
                    className="square-button-sm ms-timeline-expand"
                    bsStyle="primary"
                    tooltip={<Message msgId= {collapsed ? "timeline.expand" : "timeline.collapse"}/>}>
                    <Glyphicon glyph={collapsed ? 'chevron-up' : 'chevron-down'}/>
                </Button>

            </div>
            {!timelineIsReady && <div className="timeline-loader">
                <Loader size={50} />
            </div>}
            {!collapsed &&
                <Timeline
                    offsetEnabled={offsetEnabled}
                    playbackEnabled
                    hideLayersName={hideLayersName}
                    timelineLayers={layers}
                />}
        </div>);
    }
);

export default {
    name: __MAPSTORE_EXTENSION_CONFIG__.name,
    component: ExtensionPlugin,
    reducers: {
        dimension: require('../reducers/dimension').default,
        timeline: require('../reducers/timeline').default        
    },
    epics: require('../epics/timeline').default,
    containers: {}
};
