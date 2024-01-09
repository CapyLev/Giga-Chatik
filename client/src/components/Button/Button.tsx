import { FC, MouseEvent } from 'react';
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
    <button className="action" onClick={handleClick}>
      {buttonText}
    </button>
  );
};

export default Button;
