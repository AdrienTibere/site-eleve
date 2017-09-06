import React, {Component} from 'react';
import Divider from 'muicss/lib/react/divider';
import {server_url} from './config.js';
import {Link} from 'react-router-dom';
import fetch from 'isomorphic-fetch';
import {connect} from 'react-redux';
import ProfileScore from './ProfileScore'

class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      current_chapter: {'id': 0},
      objectives: []
    };
  }

  componentDidMount() {
    // Get current chapter
    fetch(server_url + 'api/profile/' + this.props.user.id)
    .then(response => response.json())
    .then((json) => {
      this.setState({
        current_chapter: json.current_chapter,
        objectives: json.objectives});
    });

    // Get objectives and scores

  }

  render() {
    let rows = [];
    // objectives = [{'objective': blabla, 'score': {objective, user, score}}, ...]
    this.state.objectives.forEach((obj) => {
      rows.push(
        <ProfileScore key={obj.objective.id} chapter={this.state.current_chapter} objective={obj.objective} score={obj.score.score}/>
      )
    });

    return (
      <div id="profile">
        <Link to={{pathname:'/exercices/chapitre/' + this.state.current_chapter.id, state:{chapter:this.state.current_chapter}}}>
          <div className="big-title" style={{color: this.state.current_chapter.color}}>En ce moment : Chapitre {this.state.current_chapter.nb}, {this.state.current_chapter.name}</div>
        </Link>
        <Divider />
        <div className="big-title" style={{color: this.state.current_chapter.color, display: "inline-flex"}}>Progression des objectifs :</div>
        <div id="scores-list" style={{display: "inline-flex"}}>
          <ul>
            {rows}
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
