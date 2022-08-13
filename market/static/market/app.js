const setClass = (event)=>{
    console.log(event.target.class);
    event.target.classList.add('active')
    event.target.classList.remove('unactive')
    console.log(event.target);
}


if (window.innerWidth > 424){
    const stickyElem = document?.querySelector(".sticky-div");
    const stickyElem2 = document?.querySelector(".sticky-div2");
    const stickyElem3 = document?.querySelector(".sticky-background");
    const stickyElem4 = document?.querySelector(".sticky-background2");

    const currStickyPos = ( stickyElem.getBoundingClientRect().top + window.pageYOffset - 10);
    const currStickyPos2 = ( stickyElem.getBoundingClientRect().top + window.pageYOffset - 10 - 35.3);

    window.onscroll = function() {
        if(window.pageYOffset > currStickyPos) {
            stickyElem.style.position = "fixed";
            stickyElem.style.top = "10px";
            stickyElem.style.zIndex = "10";
            stickyElem.style.width = "100%"

            if(window.pageYOffset > currStickyPos2) {
                stickyElem2.style.position = "fixed";
                stickyElem2.style.top = "45.3px";
                stickyElem2.style.zIndex = "9";
                stickyElem2.style.width = "100%"
                stickyElem2.style.marginTop = "15px"

                stickyElem3.display = "display"
                stickyElem3.style.width = "100%"
                stickyElem3.style.height = "78.83px"

                stickyElem4.display = "display"
                stickyElem4.style.position = "fixed";
                stickyElem4.style.width = "100%"
                stickyElem4.style.height = "105px"
                stickyElem4.style.zIndex = "5";
                stickyElem4.style.top = "0px";
            } else {
                stickyElem2.style.position = "initial";
                stickyElem2.style.top = "initial";
                stickyElem2.style.marginTop = "0rem"
                stickyElem2.style.zIndex = "0";
                stickyElem2.style.marginTop = "15px"

                stickyElem3.display = "None"
                stickyElem3.style.width = "0px"
                stickyElem3.style.height = "0px"

                stickyElem4.display = "None"
                stickyElem4.style.width = "0px"
                stickyElem4.style.height = "0px"
                stickyElem4.style.top = "0px";
                stickyElem4.style.position = "relative";
            }
        } else {
            stickyElem.style.position = "initial";
            stickyElem.style.top = "initial";
            stickyElem.style.marginTop = "0rem"
            stickyElem.style.zIndex = "0";

            stickyElem2.style.position = "initial";
            stickyElem2.style.top = "initial";
            stickyElem2.style.marginTop = "0rem"
            stickyElem2.style.zIndex = "0";
            stickyElem2.style.marginTop = "15px"

            stickyElem3.display = "None"
            stickyElem3.style.width = "0px"
            stickyElem3.style.height = "0px"

            stickyElem4.display = "None"
            stickyElem4.style.width = "0px"
            stickyElem4.style.height = "0px"
            stickyElem4.style.top = "0px";
            stickyElem4.style.position = "relative";
        }
    }
}else{
    const stickyElem = document?.querySelector(".sticky-div");
    const stickyElem2 = document?.querySelector(".sticky-div2");
    const stickyElem3 = document?.querySelector(".sticky-background");
    const stickyElem4 = document?.querySelector(".sticky-background2");

    const currStickyPos = ( stickyElem.getBoundingClientRect().top + window.pageYOffset - 10);
    const currStickyPos2 = ( stickyElem.getBoundingClientRect().top + window.pageYOffset - 10 - 35.3);

    window.onscroll = function() {
        if(window.pageYOffset > currStickyPos) {
            stickyElem.style.position = "fixed";
            stickyElem.style.top = "10px";
            stickyElem.style.zIndex = "10";
            stickyElem.style.width = "100%"

            if(window.pageYOffset > currStickyPos2) {
                stickyElem2.style.position = "fixed";
                stickyElem2.style.top = "74.1px";
                stickyElem2.style.zIndex = "9";
                stickyElem2.style.width = "100%"
                stickyElem2.style.marginTop = "15px"

                stickyElem3.display = "display"
                stickyElem3.style.width = "100%"
                stickyElem3.style.height = "107.63px"

                stickyElem4.display = "display"
                stickyElem4.style.position = "fixed";
                stickyElem4.style.width = "100%"
                stickyElem4.style.height = "140px"
                stickyElem4.style.zIndex = "5";
                stickyElem4.style.top = "0px";
            } else {
                stickyElem2.style.position = "initial";
                stickyElem2.style.top = "initial";
                stickyElem2.style.marginTop = "0rem"
                stickyElem2.style.zIndex = "auto";
                stickyElem2.style.marginTop = "15px"

                stickyElem3.display = "None"
                stickyElem3.style.width = "0px"
                stickyElem3.style.height = "0px"

                stickyElem4.display = "None"
                stickyElem4.style.width = "0px"
                stickyElem4.style.height = "0px"
                stickyElem4.style.top = "0px";
                stickyElem4.style.position = "relative";
            }
        } else {
            stickyElem.style.position = "initial";
            stickyElem.style.top = "initial";
            stickyElem.style.marginTop = "0rem"
            stickyElem.style.zIndex = "auto";

            stickyElem2.style.position = "initial";
            stickyElem2.style.top = "initial";
            stickyElem2.style.marginTop = "0rem"
            stickyElem2.style.zIndex = "auto";
            stickyElem2.style.marginTop = "15px"

            stickyElem3.display = "None"
            stickyElem3.style.width = "0px"
            stickyElem3.style.height = "0px"

            stickyElem4.display = "None"
            stickyElem4.style.width = "0px"
            stickyElem4.style.height = "0px"
            stickyElem4.style.top = "0px";
            stickyElem4.style.position = "relative";
        }
    }
}