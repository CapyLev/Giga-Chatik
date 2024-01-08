import { FC, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ServerImage } from "../../interfaces/server.interface";
import Icon from "../Icon/Icon";
import "./UserNavigateBar.scss";


const UserNavigateBar: FC = () => {
  const [servers, setServers] = useState<ServerImage[]>([]);

  useEffect(() => {}, []);

  return (
    <div className="navigationContainer">
      <div className="topSection">
        <Link to={"home"}>
          <Icon src="home.svg" alt="Home" />
        </Link>
      </div>

      <div className="line"></div>

      <div className="centerSection">
        {servers
          ? servers.map((server) => (
              <div key={server.id} className="Icon">
                <Icon src={server.image} alt={`Server ${server.id}`} />
              </div>
            ))
          : []}
      </div>

      <div className="line"></div>

      <div className="bottomSection">
        <Link to={"/user/profile"}>
          <Icon src="/profile.svg" alt="Home" width={55} height={55} />
        </Link>
      </div>
    </div>
  );
};

export default UserNavigateBar;