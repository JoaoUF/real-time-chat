import React from "react";

export default function TestWS() {
  const [user, setUser] = React.useState();
  const [listInformation, setListInformation] = React.useState("");
  const chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/`);

  chatSocket.onopen = function () {
    console.log("open connection!");
    console.log("subscribet to connection history");
    chatSocket.send(
      JSON.stringify({
        id: 1,
        action: "subscribe_to_connection_history",
      })
    );
    console.log("change to online status");
    chatSocket.send(
      JSON.stringify({
        action: "change_connection_history_online",
      })
    );
    console.log("get the list detail!");
    chatSocket.send(
      JSON.stringify({
        action: "list_user_chat",
      })
    );
  };

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    switch (data.type) {
      case "update_connection_history":
        setUser(data.user);
        break;
      case "list_chat_users":
        setListInformation(data.data);
        break;
      default:
        break;
    }
  };

  chatSocket.onclose = function (e) {
    console.log("Chat socket closed unexpectaly!");
  };

  return (
    <div>
      <h1>enter user</h1>
      {user}
      <h1>detail information</h1>
      {listInformation}
    </div>
  );
}
