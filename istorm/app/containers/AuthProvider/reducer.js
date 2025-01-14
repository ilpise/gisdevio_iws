/*
 *
 * Auth reducer
 *
 */
import produce from 'immer';
import moment from "moment";
import { STOP_LOADING, SYNC_AUTH, REQUEST_LOGIN,
      UPDATE_SETTINGS_SUCCESS, REQUEST_UPDATE_SETTINGS, REQUEST_SETTINGS, SETTINGS_SUCCESS,
      REQUEST_LOGOUT, REQUEST_PROFILE, REQUEST_PROFILE_SUCCESS,
      REQUEST_REFRESH, REQUEST_LOGIN_SUCCESS, REQUEST_LOGOUT_SUCCESS,
      REQUEST_ERROR, REQUEST_REFRESH_SUCCESS, REQUEST_NOTIFICATION,
      REQUEST_NOTIFICATION_SUCCESS, DELETE_NOTIFICATION, UPDATE_NOTIFICATION } from './constants';

export const initialState = {
  loading: false,
  loggingout: false,
  user: {
    email: ""
  },
  settings: {},
  error: null,
  oauth: {
    token: null,
    refreshToken: null,
    expire_at: null
  },
  notifications: {
    loading: false,
    error: null,
    results: []
  }
};

/* eslint-disable default-case, no-param-reassign */
const authReducer = (state = initialState, action) =>
  produce(state, ( draft ) => {
    switch (action.type) {
      case STOP_LOADING:
          draft.loading = false;
        break;
      case SYNC_AUTH:
          draft.oauth = action.request.oauth;
          draft.user = action.request.user;
          draft.settings = action.request.settings;
        break;
      case REQUEST_LOGIN:
          draft.loading = true;
          draft.loggingout = false;
        break;
      case REQUEST_LOGIN_SUCCESS:
          draft.loading = false;
          draft.error = initialState.error;
          draft.oauth.token = action.result.access_token;
          draft.oauth.refreshToken = action.result.refresh_token;
          draft.oauth.expire_at = moment().add((action.result.expires_in - (60 * 30)), 'seconds').unix();
        break;
      case REQUEST_LOGOUT:
          draft.loading = true;
          draft.loggingout = true;
        break;
      case REQUEST_LOGOUT_SUCCESS:
          draft.loading = false;
          draft.error = initialState.error;
          draft.oauth = initialState.oauth
        break;
      case REQUEST_REFRESH:
          draft.loading = true;
        break;
      case REQUEST_REFRESH_SUCCESS:
          draft.loading = false;
          draft.error = initialState.error;
        break;
      case REQUEST_PROFILE:
          draft.loading = true;
          draft.error = initialState.error;
        break;
      case REQUEST_PROFILE_SUCCESS:
          draft.loading = false;
          draft.error = initialState.error;
          draft.user = action.result;
        break;
      case REQUEST_NOTIFICATION:
          draft.notifications.loading = true;
          draft.notifications.error = initialState.notifications.error;
          draft.notifications.results = []
      break;
      case REQUEST_NOTIFICATION_SUCCESS:
          draft.notifications.loading = false;
          draft.notifications.error = initialState.notifications.error;
          draft.notifications.results = action.result;
          break;
      case DELETE_NOTIFICATION:
          draft.notifications.loading = true;
          draft.notifications.error = initialState.notifications.error;
         // draft.notifications.results = []
          break;
      case UPDATE_NOTIFICATION:
          draft.notifications.loading = true;
          draft.notifications.error = initialState.notifications.error;
          // draft.notifications.results = []
          break;
      case REQUEST_ERROR:
          draft.loading = false;
          draft.error = action.error;
      case REQUEST_UPDATE_SETTINGS:
          draft.loading = true;
        break;
      case UPDATE_SETTINGS_SUCCESS:
          draft.loading = false;
          draft.settings = action.result;
        break;
      case REQUEST_SETTINGS:
          draft.loading = true;
        break;
      case SETTINGS_SUCCESS:
          draft.loading = false;
          draft.settings = action.result;
        break;
    }
  });

export default authReducer;
