import {
  configureStore,
  getDefaultMiddleware,
  createSlice
} from "@reduxjs/toolkit"
import rootSaga from "./sagas"
import createSagaMiddleware from 'redux-saga'

const sagaMiddleware = createSagaMiddleware()

const middleware = [
  ...getDefaultMiddleware(),
  sagaMiddleware,
]

const alertState = {
  alerts: [],
  all_alerts: [],
  gappers: [],
  replay_time: '',
  replay_date: '06-05-2020',
}

const alertSlice = createSlice({
  name: "alert",
  initialState: alertState,
  reducers: {
    retrieveGappersSuccess:(state, action) => {
      console.log(action)
      state.gappers = action.gappers;
      return state
    },
    retrieveAlertsSuccess: (state, action) => {
      state.all_alerts = action.alerts;
      return state
    },
    retrieveAlertsFailed: (state, action) => {
      state.error = action.payload
      return state
    },
    replayTimeUpdated:(state, action) => {
      state.replay_time = action.payload.replay_time
      if (action.payload.replay_date != state.replay_date) {
        state.replay_date = action.payload.replay_date
      }
      if (state.all_alerts.length > 0) {
        state.alerts = state.all_alerts.filter(alert => {
          return alert.time <= action.payload.replay_time
        })
      }
      return state
    }
  }
})

const {
  retrieveGappersSuccess,
  retrieveAlertsSuccess,
  retrieveAlertsFailed,
  replayTimeUpdated
} = alertSlice.actions
const alertReducer = alertSlice.reducer

const store = configureStore({
  reducer: {
    alert: alertReducer,
  },
  middleware,
})
sagaMiddleware.run(rootSaga)

export {
  store,
  retrieveGappersSuccess,
  retrieveAlertsFailed,
  retrieveAlertsSuccess,
  replayTimeUpdated
}