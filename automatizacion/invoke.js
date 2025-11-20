import { LambdaClient, InvokeCommand } from "@aws-sdk/client-lambda";
import fs from "fs";

const lambda = new LambdaClient({
  region: "us-east-1",
});

async function invoke() {
  const payload = JSON.parse(fs.readFileSync("event.json", "utf8"));

  const command = new InvokeCommand({
    FunctionName: "get-proyectos-portafolio-lambda",
    Payload: Buffer.from(JSON.stringify(payload)),
    LogType: "Tail",
  });

  const response = await lambda.send(command);

  console.log("📄 Logs:");
  console.log(Buffer.from(response.LogResult, "base64").toString());

  console.log("\n📥 Respuesta:");
  console.log(Buffer.from(response.Payload));
}

invoke();
