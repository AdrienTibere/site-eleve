import React from 'react';
import {connect} from 'react-redux';
import {setRedirectUrl} from './actions.js';

class EnsureLoggedInContainer extends React.Component {
  componentDidMount() {
    const { dispatch, currentURL } = this.props;

    if (!this.props.isLoggedIn) {
      // set the current url/path for future redirection (we use a Redux action)
      // then redirect (we use a React Router method)
      dispatch(setRedirectUrl(currentURL));
      //browserHistory.replace('/')
    }
  }

  render() {
    if (this.props.isLoggedIn) {
      return (
        <div>
        {this.props.children}
        </div>
      )
    } else {
      return null
    }
  }
}

function mapStateToProps(state, ownProps) {
  return {
    isLoggedIn: state.isLoggedIn,
    currentURL: ownProps.location.pathname
  }
}

export default connect(mapStateToProps)(EnsureLoggedInContainer)
