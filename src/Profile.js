import React, {Component} from 'react';
import Divider from 'muicss/lib/react/divider';
import {server_url} from './config.js';
import {Link} from 'react-router-dom';
import fetch from 'isomorphic-fetch';
import {connect} from 'react-redux';
import ProfileChapter from './ProfileChapter'

class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      current_chapter: {'id': 0},
      current_objectives: [],
      past_chapters: []
    };
  }

  componentDidMount() {
    // Get Profile data
    fetch(server_url + 'api/profile/' + this.props.user.id)
    .then(response => response.json())
    .then((json) => {
      console.log(json);
      this.setState({
        current_chapter: json.current_chapter,
        current_objectives: json.current_objectives,
        past_chapters: json.past_chapters});
    });
  }

  render() {
    let chapters = [];
    this.state.past_chapters.forEach((obj) => {
      chapters.push(
        <ProfileChapter chapter={obj.chapter} objectives={obj.objectives} />
      )
    });
    return (
      <div id="profile">
        <div className="big-title" style={{color: this.state.current_chapter.color}}>En ce moment...</div>
        <div style={{marginBottom: "30px"}}>
          <ProfileChapter chapter={this.state.current_chapter} objectives={this.state.current_objectives} />
        </div>
        <Divider />
        <div className="big-title" style={{color: "#82B1FF", display: "flex"}}>Chapitres précédents :</div>
        <div style={{display: "inline-flex"}}>
          <ul>
            {chapters}
          </ul>
        </div>
      </div>
    )
  }
}

function mapStateToProps(state) {
  return {
    user: state.user
  }
}

export default connect(mapStateToProps)(Profile);
