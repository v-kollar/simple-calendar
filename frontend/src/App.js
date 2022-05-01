import React, { Component } from "react";
import Navbar from "./components/navbar";
import { BrowserRouter as Router } from "react-router-dom";
import axios from "axios";

class App extends Component {
  state = {
    //Static scheduled Events to know if something is wrong.
    scheduledEvents: [
      {
        id: 1,
        title: "Connection lost",
        startDate: "2020-04-10T13:00:00",
        endDate: "2030-04-10T15:00:00",
      },
    ],
    currentDate: new Date(),

    //Connstring with backend
    connString: "xXx",
  };

  constructor(props) {
    super(props);
    this.commitChanges = this.commitChanges.bind(this);
  }

  componentDidMount() {
    console.log("IHAAAA");
  }

  commitChanges({ added, changed, deleted }) {
    this.setState((state) => {
      let { scheduledEvents } = state;

      if (added) {
        //added = object (title, startDate, endDate)
        console.log("ADDED");
      }

      if (changed) {
        //changed = {Id : object (startDate, endDate)}
        console.log("CHANGED");
      }

      if (deleted !== undefined) {
        //deleted = Id
        console.log("DELETED");
      }

      return { scheduledEvents };
    });
  }

  render() {
    return (
      <Router>
        <Navbar
          scheduledEvents={this.state.scheduledEvents}
          currentDate={this.state.currentDate}
          commitChanges={this.commitChanges}
        />
      </Router>
    );
  }
}

export default App;
