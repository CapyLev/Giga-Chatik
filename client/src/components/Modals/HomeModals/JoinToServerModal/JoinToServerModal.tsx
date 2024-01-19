import React, { FC, useState } from "react";
import { ModalProps } from "../../../../interfaces/common.interface";
import "../../ModalsGlobal.scss";
import "./JoinToServerModal.scss";

const JoinToServerModal: FC<ModalProps> = ({ closeModal }) => {
  const [serverId, setServerId] = useState<string>("");
  const [isPrivate, setIsPrivate] = useState<boolean>(false);
  const [serverPassword, setServerPassword] = useState<string>("");

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
    // доделать эту хуету
    // нужно отправить сразу запрос без никаких проверок
    // отловить ошибку
    // нас интересует только одна ошибка и это если пароль неверн.
    // на сервере надо поменять скорее всего статус код
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
