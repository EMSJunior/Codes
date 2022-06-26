import React from 'react'
import GlobalStyle from './styles/Global'
import RoutesApp from './routes'
import { AuthProvider } from './contexts/auth'

const App = () => {
  return (
    <AuthProvider>
      <div>Appicar</div>
      <GlobalStyle />
    </AuthProvider>
  )
}

export default App