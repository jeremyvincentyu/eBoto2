import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "@nomicfoundation/hardhat-ignition-ethers"

const config: HardhatUserConfig = {
  networks: {
    hardhat:{
      accounts:{
        count: 50,
      }
      ,
      eboto: {
        url:"http://127.0.0.1:8545/",
        accounts: ["0x3ccca6c7deb7bef6f599634e7fcdb7765eaf8f228f18fb46e74ea09a2d638e08"]
      }
    }
  },
  solidity: "0.8.19",
};

export default config;
