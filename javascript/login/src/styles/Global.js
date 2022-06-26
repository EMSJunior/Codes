import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    width: 100vw;
    height: 100vw;
    backgroud-color: #f4f4f4:
    font-family: Arial, Helvetica, sans-serif
  }
`;

export default GlobalStyle;