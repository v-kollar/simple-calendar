import * as React from "react";
import { Paper } from "@mui/material";
import {
  ViewState,
  EditingState,
  IntegratedEditing,
} from "@devexpress/dx-react-scheduler";
import {
  Scheduler,
  Appointments,
  AppointmentForm,
  AppointmentTooltip,
  DragDropProvider,
  AllDayPanel,
  DayView,
  Toolbar,
  DateNavigator,
  TodayButton,
} from "@devexpress/dx-react-scheduler-material-ui";

//Dayview component
const Day = ({
  scheduledEvents,
  currentDate,
  setDate,
  commitChanges,
  AppointmentStyle,
}) => {
  return (
    <Paper>
      <Scheduler data={scheduledEvents}>
        <ViewState
          onCurrentDateChange={setDate}
          defaultCurrentDate={currentDate}
        />
        <EditingState onCommitChanges={commitChanges} />
        <IntegratedEditing />
        <DayView />
        <AllDayPanel />
        <Toolbar />
        <DateNavigator />
        <TodayButton />
        <Appointments appointmentComponent={AppointmentStyle} />
        <AppointmentTooltip showOpenButton showDeleteButton />
        <AppointmentForm />
        <DragDropProvider />
      </Scheduler>
    </Paper>
  );
};

export default Day;
