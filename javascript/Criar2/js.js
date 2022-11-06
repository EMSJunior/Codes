const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");

const myGroupName = "Robótica - Outubro";

const linkmsg = "https://chat.whatsapp.com/Cqo6x2CiOcu5CQMedbZ2jX"

const contatos = ["553891129252@c.us","553888070457@c.us","553899592562@c.us","553891725442@c.us","553899438581@c.us","553891648854@c.us","553884020372@c.us","553888193109@c.us","553891885444@c.us","553884240142@c.us","553899608945@c.us","553891771974@c.us","553888343585@c.us","553892048922@c.us","553899424152@c.us","553899778760@c.us","553892265309@c.us","553888645181@c.us","553898697740@c.us"]

//const contatos = ["553899670236@c.us"];

const invitemsg = "Olá, Boa noite! Te adicionei ao grupo de Robótica! Caso não tenha sido adicionado, entre pelo link: " + linkmsg
const client = new Client({
  authStrategy: new LocalAuth(),
});

client.on("qr", (qr) => {
  qrcode.generate(qr, { small: true });
});


client.on("ready", () => {
  console.log("Client is ready!");
  client.getChats().then((chats) => {
    const myGroup = chats.find((chat) => chat.name === myGroupName);

      
        for (let id of contatos){
          try{
        myGroup
          .addParticipants([id]) // Pass an array of contact IDs [id1, id2, id3 .....]
          .then(() => client.sendMessage(id, invitemsg));            
          }catch(e){console.log(id)}
        }




  });
});

client.initialize();