$(".dialog-fase").dialog({
    autoOpen: false,
    height: 290,
    width: 540,
    resizable: false,
    modal: true,
    show: {
        effect: "scale",
        duration: 300
    },
    hide: {
        effect: "scale",
        duration: 300
    }
});

$("#nao-implementado").dialog({
    autoOpen: false,
    width: 320,
    height: 140,
    resizable: false,
    modal: true,
    show: {
        effect: "scale",
        duration: 300
    },
    hide: {
        effect: "scale",
        duration: 300
    }
});

$(".fase").click(function() {
    var $this = $(this);
    if ($this.hasClass("not")) {
        $("#nao-implementado").dialog("open");
        return false;
    }
    if ($this.hasClass("fase-1")) {
        $("#dialog-fase1").dialog("open");
        return false;
    }
});
