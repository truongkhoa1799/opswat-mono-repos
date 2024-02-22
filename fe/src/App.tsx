import * as React from "react";
import AppRoutes from "./AppRoutes";
import { ErrorBoundary } from "react-error-boundary";
import { HelmetProvider } from "react-helmet-async";
import { QueryClientProvider, QueryClient } from "react-query";
import PartialError from "./components/organisms/PartialError";
import { ReactQueryDevtools } from "react-query/devtools";
import Axios from "axios";
import config from "./config";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: (failureCount: number, error: any): boolean => {
        if (Axios.isAxiosError(error) && error.message === "Network Error" && failureCount <= 3) {
          return true;
        }
        return false;
      },
    },
  },
});

export default function App() {
  return (
    <HelmetProvider>
      <QueryClientProvider client={queryClient}>
        <ErrorBoundary FallbackComponent={PartialError}>
          <AppRoutes />
          {config["env"] !== "prod" && <ReactQueryDevtools position="bottom-right" />}
        </ErrorBoundary>
      </QueryClientProvider>
    </HelmetProvider>
  );
}
