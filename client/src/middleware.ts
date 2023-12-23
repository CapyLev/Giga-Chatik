import { NextRequest, NextResponse } from "next/server";

export async function middleware(request: NextRequest): Promise<NextResponse> {
  // TODO: добавить проверку на наличие токена

  return NextResponse.next();
}

export const config = {
  matcher: ["/home/:slug*"],
};
