import { useState } from "react";
import { Button } from "../../components";
import "./HomePage.scss";
import CreateServerModal from "../../components/Modals/HomeModals/CreateServerModal/CreateServerModal";
import JoinToServerModal from "../../components/Modals/HomeModals/JoinToServerModal/JoinToServerModal";

const HomePage = () => {
  const [isJoinToServerModalOpened, setJoinToServerModalOpened] =
    useState<boolean>(false);
  const [isCreateServerModalOpened, setCreateServerModalOpened] =
    useState<boolean>(false);

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
