import {LOG_IN, SET_REDIRECT_URL, REQUEST_LOG_IN, RECEIVE_LOG_IN} from './actions.js';

const initialState = {
  user: {},
  isLoggedIn: false,
  redirectUrl: '/'
}

function mainReducer(state = initialState, action) {
  switch (action.type) {
    case LOG_IN:
      return Object.assign({}, state, {
        isLoggedIn: true,
        user: action.user
      })
    case SET_REDIRECT_URL:
      return Object.assign({}, state, {
        redirectUrl: action.newUrl
      })
		case REQUEST_LOG_IN:
			return Object.assign({}, state, {
				isFetching: true,
			})
		case RECEIVE_LOG_IN:
			return Object.assign({}, state, {
				isFetching: false,
				isLoggedIn: true,
				user: action.user
			})
    default: return state
  }
}

export default mainReducer
