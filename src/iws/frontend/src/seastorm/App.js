import React from 'react';
import { Provider } from 'react-redux';
import AppRoutes from './routes';
import D6Routes from './d6routes';
import { store } from './store';

// Log the initial state
console.log('Initial state: ', store.getState())

import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AuthLoader from './modules/Auth';

const App = () => {
  return (
    <>
      <Provider store={store}>
        <AuthLoader>
          <AppRoutes />
          <D6Routes />
        </AuthLoader>
      </Provider>
      <ToastContainer 
        position="top-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
      />
    </>
  )
}

export default App
