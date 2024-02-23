type Config = {
  env: string;
  API_URL: string;
};

const dev: Config = {
  env: "dev",
  API_URL: "http://localhost:8000",
};

const prod: Config = {
  env: "prod",
  API_URL: "http://localhost:8000",
};

const configs: { [key: string]: Config } = {
  dev,
  prod,
};

let env = process.env.APP_ENV;
if (env === undefined) {
  env = "dev";
}

export default configs[env];
