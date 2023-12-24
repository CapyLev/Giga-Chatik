/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    BASE_URL: process.env.BASE_URL,
  },
  images: {
    domains: ['media.istockphoto.com'],
  },
}

module.exports = nextConfig
