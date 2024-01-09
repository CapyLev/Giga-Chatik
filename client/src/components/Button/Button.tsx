import { FC, MouseEvent } from "react";
import "./Button.scss";

interface ButtonProps {
  onClickHandler: () => void;
  buttonText: string;
}

const Button: FC<ButtonProps> = ({ onClickHandler, buttonText }) => {
  const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    onClickHandler();
  };

  return (
    <div className="action">
      <button onClick={handleClick}>{buttonText}</button>
    </div>
  );
};

export default Button;
