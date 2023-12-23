import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";
import { config as globalConfig } from "@/utils/config";
import { Routers } from "./utils/common";

export async function middleware(request: NextRequest): Promise<NextResponse> {
  if (!cookies().has(globalConfig.auth.cookieName)) {
    return NextResponse.redirect(new URL(Routers.WELCOME, request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/home"],
};
