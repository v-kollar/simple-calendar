import * as React from "react";
import { Paper } from "@mui/material";
import {
  ViewState,
  EditingState,
  IntegratedEditing,
} from "@devexpress/dx-react-scheduler";
import {
  Scheduler,
  MonthView,
  Appointments,
  AppointmentForm,
  AppointmentTooltip,
  DragDropProvider,
  Toolbar,
  DateNavigator,
  TodayButton,
  AllDayPanel,
} from "@devexpress/dx-react-scheduler-material-ui";

//Monthview component
const Month = ({
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
        <MonthView />
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

export default Month;
