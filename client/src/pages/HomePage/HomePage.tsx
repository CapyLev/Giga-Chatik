import { useState } from "react";
import { Button } from "../../components";
import "./HomePage.scss";

const HomePage = () => {
  const [isJoinToServerModalOpened, setJoinToServerModalOpened] =
    useState<boolean>(false);
  const [isCreateServerModalOpened, setCreateServerModalOpened] =
    useState<boolean>(false);

  const handleJoinToServerBtn = () => {};
  const handleCreateServerBtn = () => {};

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
      {/* {isJoinToServerModalOpened && <... closeModal={closeModal} />}
      {isCreateServerModalOpened && <... closeModal={closeModal} />} */}
    </div>
  );
};

export default HomePage;
