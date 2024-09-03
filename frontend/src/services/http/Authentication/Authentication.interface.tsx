export interface Register {
  email: string;
  password1: string;
  password2: string;
}

export interface Login {
  email: string;
  password: string;
}

export interface User {
  pk: number;
  email: string;
  first_name: string;
  last_name: string;
}

export interface LoginSuccesful {
  access: string;
  refresh: string;
  user: User;
  access_expiration: Date;
  access_refresh: Date;
}

export interface RefreshToken {
  access: string;
  access_expiration: Date;
}
