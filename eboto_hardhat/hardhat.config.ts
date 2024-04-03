import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "@nomicfoundation/hardhat-ignition-ethers"

const config: HardhatUserConfig = {
  networks: {
    hardhat:{
      accounts:{
        count: 50,
      }

    }
  },
  solidity: "0.8.19",
};

export default config;
