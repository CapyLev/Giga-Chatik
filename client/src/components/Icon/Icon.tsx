import { FC } from "react";
import Image from "next/image";
import styles from "./Icon.module.scss";

interface IconProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
}

const Icon: FC<IconProps> = ({ src, alt, width = 55, height = 55 }) => {
  return (
    <div>
      <Image
        className={styles.Icon}
        src={src}
        alt={alt}
        width={width}
        height={height}
      />
    </div>
  );
};

export default Icon;
