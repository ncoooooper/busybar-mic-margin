import {marks} from "./front";
import {instrument} from "@shared/instrument";

instrument({
  marks,
  "title": "MIC MARGIN",
  "primary": "Mic Margin",
  "accent": "#F5A950",
  "cadence": 1800,
  "motion": {enabled:false},
  "setup": "Start companion/serve.py"
});
