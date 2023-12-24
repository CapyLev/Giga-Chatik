"use client";

import Link from "next/link";
import Image from "next/image";
import { FC, useEffect, useState } from "react";
import styles from "./NavigateBar.module.scss";
import { Routers } from "@/utils/common";
import { fetchServerIcons } from "@/services/navbar.service";
import { ServerImage } from "@/interfaces/server.interfaces";
import Icon from "../Icon/Icon";

interface NavigateBarProps {}

const NavigateBar: FC<NavigateBarProps> = ({}) => {
  const [servers, setServers] = useState<ServerImage[]>([]);

  useEffect(() => {
    fetchServerIcons().then((serversResponse) => {
      setServers(serversResponse.result);
    });
  }, []);

  return (
    <div className={styles.navigationContainer}>
      <div className={styles.topSection}>
        <Link href={Routers.HOME}>
          <Icon src="home.svg" alt="Home" />
        </Link>
      </div>

      <div className={styles.line}></div>

      <div className={styles.centerSection}>
        {servers
          ? servers.map((server) => (
              <div key={server.id} className={styles.Icon}>
                <Icon src={server.image} alt={`Server ${server.id}`} />
              </div>
            ))
          : []}
      </div>

      <div className={styles.line}></div>

      <div className={styles.bottomSection}>
        <Link href={Routers.PROFILE}>
          <Icon src="/profile.svg" alt="Home" width={55} height={55} />
        </Link>
      </div>
    </div>
  );
};

export default NavigateBar;
