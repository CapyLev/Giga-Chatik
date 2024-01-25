import { FC } from "react";
import "./PublicServer.scss";

interface PublicServerProps {
  image: string;
  name: string;
  desc: string;
  countOfMembers: number;
}

const PublicServer: FC<PublicServerProps> = ({
  image,
  name,
  desc,
  countOfMembers,
}) => {

  console.log(name);
  
  return (
    <div className="block">
      <div className="image-container">
        <img src={image} alt="serverImage" />
      </div>
      <div className="text-container">
        <p className="server-name">{name}</p>
        <p className="server-desc">{desc}</p>
        <p className="member-count">{countOfMembers} members</p>
      </div>
    </div>
  );
};

export default PublicServer;
