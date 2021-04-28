import http from "k6/http";
import { sleep, check } from "k6";
import runTestOne from "./test1.js";
import runTestTwo from "./test2.js";

export default function() {
    runTestOne();
    runTestTwo();
};
