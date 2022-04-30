import React, { useState } from "react";
import "../navbar.css";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";
import Box from "@mui/material/Box";
import { Link, Route, Routes } from "react-router-dom";
import Home from "./home";
import About from "./about";
import Day from "./day";
import Week from "./week";
import Month from "./month";

const Navbar = ({
  scheduledEvents,
  currentDate,
  setDate,
  commitChanges,
  AppointmentStyle,
}) => {
  const [active, setActive] = useState(false);
  //Array of routes with important properties for components

  return (
    <React.Fragment>
      <nav className="nav">
        <Link className="nav__brand" to="/">
          Home
        </Link>
        <ul className={`nav__menu ${active ? "nav__active" : ""}`}>
          <li className="nav__item">
            <Link className="nav__link" to="/day">
              Day
            </Link>
          </li>
          <li className="nav__item">
            <Link className="nav__link" to="/week">
              Week
            </Link>
          </li>
          <li className="nav__item">
            <Link className="nav__link" to="/month">
              Month
            </Link>
          </li>
          <li className="nav__item">
            <Link className="nav__link" to="/about">
              About
            </Link>
          </li>
        </ul>

        <Box
          className={"nav__toggler"}
          onClick={() => setActive((prevActive) => !prevActive)}
        >
          {active ? (
            <CloseIcon sx={{ fontSize: 25 }} onClick={() => setActive(true)} />
          ) : (
            <MenuIcon sx={{ fontSize: 25 }} onClick={() => setActive(false)} />
          )}
        </Box>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/day"
          element={
            <Day
              scheduledEvents={scheduledEvents}
              currentDate={currentDate}
              setDate={setDate}
              commitChanges={commitChanges}
              AppointmentStyle={AppointmentStyle}
            />
          }
        />
        <Route
          path="/week"
          element={
            <Week
              scheduledEvents={scheduledEvents}
              currentDate={currentDate}
              setDate={setDate}
              commitChanges={commitChanges}
              AppointmentStyle={AppointmentStyle}
            />
          }
        />
        <Route
          path="/month"
          element={
            <Month
              scheduledEvents={scheduledEvents}
              currentDate={currentDate}
              setDate={setDate}
              commitChanges={commitChanges}
              AppointmentStyle={AppointmentStyle}
            />
          }
        />
      </Routes>
    </React.Fragment>
  );
};

/*
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/day" element={<Day />} />
        <Route path="/week" element={<Week />} />
        <Route path="/month" element={<Month />} />

        const routes = [
        {
          key: "home",
          path: "/",
          element: Home,
        },
        {
          key: "day",
          path: "/day",
          element: Day,
          scheduledEvents: { scheduledEvents },
          currentDate: { currentDate },
          setDate: { setDate },
          commitChanges: { commitChanges },
          AppointmentStyle: { AppointmentStyle },
        },
        {
          key: "week",
          path: "/week",
          element: Week,
          scheduledEvents: { scheduledEvents },
          currentDate: { currentDate },
          setDate: { setDate },
          commitChanges: { commitChanges },
          AppointmentStyle: { AppointmentStyle },
        },
        {
          key: "month",
          path: "/month",
          element: Month,
          scheduledEvents: { scheduledEvents },
          currentDate: { currentDate },
          setDate: { setDate },
          commitChanges: { commitChanges },
          AppointmentStyle: { AppointmentStyle },
        },
      ];


        {routes.map(({ key, path, element: E }) => (
          <Route
            key={key}
            path={path}
            render={(props) => (
              <E
                {...props}
                scheduledEvents={scheduledEvents}
                currentDate={currentDate}
                setDate={setDate}
                commitChanges={commitChanges}
                AppointmentStyle={AppointmentStyle}
              />
            )}
          />
        ))}

*/

export default Navbar;
