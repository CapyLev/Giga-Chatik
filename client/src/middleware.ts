import {NextRequest, NextResponse} from "next/server";

export async function middleware(request: NextRequest): Promise<NextResponse> {
    const cookie = request.cookies.get('4atik');

    if (cookie?.value) {
        return NextResponse.redirect(new URL('/home', request.url));
    } else if (request.nextUrl.pathname === '/auth') {
        return NextResponse.redirect(new URL('/home', request.url));
    }

    return NextResponse.next();
}

export const config = {
  matcher: ['/', '/auth'],
}