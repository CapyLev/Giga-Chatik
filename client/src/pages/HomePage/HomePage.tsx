import { useEffect, useState } from "react";
import { Button, Icon } from "../../components";
import * as serverService from "../../services/ServerServices/server.service";
import CreateServerModal from "../../components/Modals/HomeModals/CreateServerModal/CreateServerModal";
import JoinToServerModal from "../../components/Modals/HomeModals/JoinToServerModal/JoinToServerModal";
import { PublicServerDTO } from "../../interfaces/server.interface";
import "./HomePage.scss";

const HomePage = () => {
  const [publicServers, setPublicServers] = useState<PublicServerDTO[]>();
  const [isJoinToServerModalOpened, setJoinToServerModalOpened] =
    useState<boolean>(false);
  const [isCreateServerModalOpened, setCreateServerModalOpened] =
    useState<boolean>(false);

  useEffect(() => {
    serverService.getAllPublicServers().then((servers) => {
      setPublicServers(servers.result);
    });
  }, []);

  const closeModal = () => {
    setCreateServerModalOpened(false);
    setJoinToServerModalOpened(false);
  };

  const handleJoinToServerBtn = () => {
    setJoinToServerModalOpened(true);
  };
  const handleCreateServerBtn = () => {
    setCreateServerModalOpened(true);
  };

  return (
    <div className="home">
      <h1>WELCOME</h1>

      <div className="serverActions">
        <Button
          onClickHandler={handleJoinToServerBtn}
          buttonText="JOIN TO THE PARTY"
        />
        <Button
          onClickHandler={handleCreateServerBtn}
          buttonText="CREATE UR OWN PARTY"
        />
      </div>

      <div className="publicServers">
        <h4>Public Servers</h4>
        <div className="publicServersList">
          {/* TODO: Show public servers */}
          {publicServers
            ? publicServers.map((server) => (
              <p>server {server.name}</p>
            ))
            : []}
        </div>
      </div>

      {isJoinToServerModalOpened && (
        <JoinToServerModal closeModal={closeModal} />
      )}
      {isCreateServerModalOpened && (
        <CreateServerModal closeModal={closeModal} />
      )}
    </div>
  );
};

export default HomePage;
