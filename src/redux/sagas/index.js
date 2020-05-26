import { put, takeEvery, all, call } from 'redux-saga/effects'
import { retrieveAlertsSuccess } from '../index.js'


function* helloSaga() {
  console.log('Hello Sagas!')
}

function retrieveAlerts(replay_date) {
  console.log('Date: ', replay_date)
  return fetch(`http://localhost:8081/api/alerts?date=${replay_date}`).then(response =>
    response.json()
  );
}

function* retrieveAsync(action) {
  const payload = yield call(retrieveAlerts, action.payload)

  const alerts = payload.filter(alert => {
    return alert.strategy === 1
  })

  const gappers = payload.filter(gapper => {
    return gapper.strategy === 4
  })

  yield put({ type: 'alert/retrieveAlertsSuccess', alerts })
  yield put({type: 'alert/retrieveGappersSuccess', gappers})
}

function* watchRetrieveAsync() {
  yield takeEvery('RETRIEVE_ALERTS_ASYNC', retrieveAsync)
}

// notice how we now only export the rootSaga
// single entry point to start all Sagas at once
export default function* rootSaga() {
  yield all([
    helloSaga(),
    watchRetrieveAsync()
  ])
}