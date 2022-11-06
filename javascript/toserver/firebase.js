// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.1/firebase-app.js";
import { getDatabase, ref, get, child  } from "https://www.gstatic.com/firebasejs/9.1.1/firebase-database.js";


// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAl1K7gdZv6qE-nEaw_SmBQnMO535ux5Hw",
  authDomain: "testao-30962.firebaseapp.com",
  projectId: "testao-30962",
  storageBucket: "testao-30962.appspot.com",
  messagingSenderId: "427545093054",
  appId: "1:427545093054:web:56b1f599db196276aacfef",
  databaseURL: "https://testao-30962-default-rtdb.firebaseio.com/"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const database = getDatabase(app);

const dbref = ref(database);

var dados = get(child(dbref,'UsersData/HBRef/readings/')).then((snapshot)=>{
  if (snapshot.exists()){
    return(snapshot.val());
  }else{
    console.log('Not Available');
  }
})

var posicoes={
  'latitude': [],
  'longetude': []
}

dados.then(value => {
  for(let x in value){
    posicoes['latitude'].push(value[x]['GPS_Latitude'])
    posicoes['longetude'].push(value[x]['GPS_Longetude'])
  }
})
console.log((posicoes['latitude']))