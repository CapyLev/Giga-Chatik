import React, { FC, useState } from "react";
import { ModalProps } from "../../../../interfaces/common.interface";
import * as serverService from "../../../../services/ServerServices/server.service";
import "../../ModalsGlobal.scss";
import "./JoinToServerModal.scss";

const JoinToServerModal: FC<ModalProps> = ({ closeModal }) => {
  const [serverId, setServerId] = useState<string>("");
  const [isPrivate, setIsPrivate] = useState<boolean>(false);
  const [serverPassword, setServerPassword] = useState<string>("");
  const [error, setError] = useState<string | null>(null);

  const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  const handleServerIdChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setServerId(e.target.value);
  };

  const handleIsPrivateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsPrivate(e.target.checked);
    if (!e.target.checked) {
      setServerPassword("");
    }
  };

  const handleServerPasswordChange = (
    e: React.ChangeEvent<HTMLInputElement>,
  ) => {
    setServerPassword(e.target.value);
  };

  const handleSubmit = async () => {
    const is_password_required = await serverService.joinToServer(
      serverId,
      serverPassword,
    );

    if (is_password_required) {
      setError("Password is incorrect.");
    }
  };

  return (
    <div className="overlay" onClick={closeModal}>
      <div className="modal" onClick={handleContainerClick}>
        <div className="modalTitle">
          <h3>Join to Server</h3>
          <span className="close" onClick={closeModal}>
            &times;
          </span>
        </div>
        <div className="modalContent">
          {error && <p>{error}</p>}
          <input
            type="text"
            placeholder="Server id"
            value={serverId}
            onChange={handleServerIdChange}
            className="input"
          />
          {isPrivate && (
            <input
              type="password"
              placeholder="Server password"
              value={serverPassword}
              onChange={handleServerPasswordChange}
              className="input"
            />
          )}
          <div className="switchLabel">
            <p>Private server?</p>
            <label className="switchInput">
              <input
                type="checkbox"
                checked={isPrivate}
                onChange={handleIsPrivateChange}
              />
              <span className="slider"></span>
            </label>
          </div>
          <button onClick={handleSubmit} className="submitButton">
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};

export default JoinToServerModal;
