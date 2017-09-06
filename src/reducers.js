import {LOG_IN, LOG_OUT, SET_REDIRECT_URL, REQUEST_LOG_IN, RECEIVE_LOG_IN, AUTHENTICATE_USER} from './actions.js';

const initialState = {
  user: null,
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
    case LOG_OUT:
      return Object.assign({}, state, {
        isLoggedIn: false,
        user: null,
        redirectUrl: '/'
      })
    case SET_REDIRECT_URL:
      return Object.assign({}, state, {
        redirectUrl: action.newUrl
      })
    case AUTHENTICATE_USER:
      return Object.assign({}, state, {
        user: action.user
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
