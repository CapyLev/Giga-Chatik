import { FC } from "react";
import "./Icon.scss";

interface IconProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
}

const Icon: FC<IconProps> = ({ src, alt, width = 55, height = 55 }) => {
  return (
    <>
      <img className="Icon" src={src} alt={alt} width={width} height={height} />
    </>
  );
};

export default Icon;
