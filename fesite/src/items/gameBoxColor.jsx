import React from "react";


const timeColor = (time) => {
    const tn = "#676767"; // gray (null)
    const t0 = "#2B64BA"; // blue
    const t1 = "#42BA38"; // green
    const t2 = "#C08C26"; // orange-yellow
    const t3 = "#CA6319"; // orange
    const t4 = "#CA0000"; // red

    if (time == null) {
        return tn;
    }
    if (time < 600) { // 10 min
        return t0;
    }
    if (time < 1800) { // 30 min
        return t1;
    }
    if (time < 5400) { // 1h 30 min
        return t2;
    }
    if (time < 10800) { // 3h
        return t3;
    }

    return t4; // > 3h
}

const timeText = (time) => {
    if (time == null) {
        return `No data`;
    }

    if (time < 60) {
        return `${time} seconds`;
    }

    if (time < 3600) {
        return `${time} minutes`;
    }

    let hours = parseInt(time / 60);
    let minute = time % 60;

    return `${hours}h ${minute}min`;
}

const timeFormat = (time) => {
    return {
        color: timeColor(time),
        text:  timeText(time)
    };
}

const diffColor = () => {

}

const diffText = () => {

}

const colorBox = (funcFormat, data) => {
    if (funcFormat == null) {
        return (
            <>
                <div className="game-box">
                </div>
            </>
        );
    }

    const result = funcFormat(data);
    return (
        <>
            <div className="game-box" style={
                {
                    backgroundColor: result.color,
                }
            }>
                {result.text}
            </div>
        </>
    );
}

const BoxColorInfo = {
    colorBox,
    timeFormat
}

export default BoxColorInfo;