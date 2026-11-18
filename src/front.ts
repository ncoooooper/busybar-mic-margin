import type {Page} from "@shared/instrument";
import {rect, type Frame} from "@shared/surface";

export function marks(page: Page): Frame {
  let fraction = page.fraction;
  if (fraction === undefined) {
    if (page.value === "silence") fraction = 0;
    else if (/^-?\d+(\.\d+)?dB$/.test(page.value)) fraction = (parseFloat(page.value)+48)/48;
    else return [];
  }
  const bars = Math.round(8*Math.max(0, Math.min(1,fraction)));
  return Array.from({length:8},(_,i)=>rect("level"+i,48+i*3,13-i,2,2+i,
    i>=bars?"#303C42FF":i===7?"#F47B68FF":i>=5?"#EFB869FF":"#79CCABFF"));
}
