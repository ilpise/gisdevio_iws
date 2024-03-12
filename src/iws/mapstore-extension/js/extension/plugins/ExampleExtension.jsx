/*
 * Copyright 2021, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
*/

/*
import React from 'react';
import { connect } from 'react-redux';
import Message from "@mapstore/framework/components/I18N/Message";
import '@js/extension/assets/style.css';
*/

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createSelector } from 'reselect';
import { mapSelector } from '@mapstore/framework/selectors/map';

function Extension({
    center
}) {
    return (
        <div
            className="shadow"
            style={{
                position: 'absolute',
                zIndex: 100,
                bottom: 35,
                margin: 8,
                left: '50%',
                backgroundColor: '#ffffff',
                padding: 8,
                textAlign: 'center',
                transform: 'translateX(-50%)'
            }}
        >
            <div>
                <small>
                    Map Center ({center.crs})
                </small>
            </div>
            <div>
                x: <strong>{center?.x?.toFixed(6)}</strong>
                {' | '}
                y: <strong>{center?.y?.toFixed(6)}</strong>
            </div>
        </div>
    );
}

Extension.propTypes = {
    center: PropTypes.object
};

Extension.defaultProps = {
    center: {}
};

const ExtensionPlugin = connect(
    createSelector([
        mapSelector
    ], (map) => ({
        center: map?.center
    })),
    {}
)(Extension);

// const ConnectedExtension = connect(() => ({}))(Extension);

export default {
    name: __MAPSTORE_EXTENSION_CONFIG__.name,
    // component: ConnectedExtension,
    component: ExtensionPlugin,
    reducers: {},
    epics: {},
    containers: {}
};
