import React from 'react';
import {connect} from 'react-redux';

class EnsureLoggedInContainer extends React.Component {
  componentDidMount() {
    const { dispatch, currentURL } = this.props;

    if (!this.props.isLoggedIn) {
      // set the current url/path for future redirection (we use a Redux action)
      // then redirect (we use a React Router method)
      //dispatch(setRedirectUrl(currentURL))
      //browserHistory.replace('/')
    }
  }

  render() {
		console.log(this.props);
    if (!this.props.isLoggedIn) {
      return this.props.children
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
