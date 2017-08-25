import React, {Component} from 'react';
import ObjectiveResume from './ObjectiveResume.js';
import {server_url} from './config.js';

class ObjectivesByChapter extends Component {
  constructor(props) {
    super(props);
    let chapter = {};
    if (props.location.state) {
      chapter = props.location.state.chapter;
    }
    this.state = {
      // get chapter by id
      chapter : chapter,
      objectives: []
    };
    this.checkObj = this.checkObj.bind(this);
  }

  checkObj(obj) {
    return obj.chapter_id === this.state.chapter.id;
  }

  componentDidMount() {
    //Get current chapter
    fetch(server_url + 'api/chapter/' + this.props.match.params.chapterId.toString())
    .then(response => response.json())
    .then(responseJson => this.setState({chapter: responseJson}));
    //Get objectives from server
    fetch(server_url + 'api/chapter/' + this.props.match.params.chapterId.toString() + '/objectives')
    .then(response => response.json())
    .then((responseJson) => {this.setState({objectives: responseJson.result.sort((a,b) => a.nb-b.nb)});});
  }

  render() {
    //display objectives
    let rows = [];
    this.state.objectives.forEach((obj) => {
      rows.push(
        <ObjectiveResume key={obj.id} obj={obj} chapter={this.state.chapter} color={this.state.chapter.color}></ObjectiveResume>
      )
    });

    return (
      <div id="objectives">
        <ul>
        <div className="big-title" style={{color: this.state.chapter.color}}>Chapitre {this.state.chapter.nb} : {this.state.chapter.name}</div>
        {rows}
        </ul>
      </div>
    )
  }
}

export default ObjectivesByChapter
