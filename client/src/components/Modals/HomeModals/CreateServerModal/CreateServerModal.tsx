import { FC, useState } from "react";
import { ModalProps } from "../../../../interfaces/common.interface";
import "../../ModalsGlobal.scss";

const CreateServerModal: FC<ModalProps> = ({ closeModal }) => {
  const handleContainerClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  return (
    <div className="overlay" onClick={closeModal}>
      <div className="modal" onClick={handleContainerClick}>
        <span className="close" onClick={closeModal}>
          &times;
        </span>
        <div className="modalContent"></div>
      </div>
    </div>
  );
};

export default CreateServerModal;
