<!DOCTYPE html>
<html lang="en">
<head>
    <!-- stylesheets -->
    <link rel="stylesheet" href = "../css/bootstrap.min.css">
    <link rel="stylesheet" href = "../css/bootstrap-grid.css">
    <link rel="stylesheet" href = "../css/art-style.css">
    <link rel="stylesheet" href = "../css/art-country-style.css">
    <?php
    $db = new PDO("sqlite:current_unohca.db");
    $sql = 'SELECT DISTINCT * FROM syria WHERE days_in_db > (SELECT MAX(days_in_db) FROM syria) - 7 ORDER BY score DESC';
    $result = $db->query($sql);
    $rowarray = $result->fetchall(PDO::FETCH_ASSOC);
    $x = 0;

    function show($rowarray){
        global $x;
        $title = $rowarray[$x]['title'];
        echo "$title";
    };
    
    function show2($rowarray){
        global $x;
        $url = $rowarray[$x]['url'];
        echo "<a class='art-div-link' href='$url'></a>";       
        $x++;
    }
    ?>
</head>
<body>
    <nav class="navbar navbar-expand navbar-dark fixed-top art-style-back-black">
      <a href="../index.html" class="pull-left"><img src="../img/vertical/navbar.png" width="35px" height="30px"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#art-navbarCollapse" aria-controls="art-navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="art-navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="../other-pages/countries.html">Countries</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../other-pages/about.html">About</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container-fluid syria-div-page">
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-3 col-1"></div>
            <div class="col-md-6 col-10 art-style-back-red art-container-country">
                <p class="country-name-text art-unselectable">Syria</p>
            </div>
            <div class="col-md-3 col-1"></div>
        </div>
        <div class="row art-style-15-height"></div>
        <div class="row">
            <div class="col-md-6 col-2"></div>
            <div class="col-md-5 col-8 art-style-back-red">
                <div class="row art-container-country">
                    <div class="col-12 art-style-white-3-bborder">
                        <p class="text-uppercase art-country-title-style art-unselectable">Summary:</p>
                    </div>
                    <div class="col-12">
                        <p class="art-style-text-white sec-font art-style-margins-country art-unselectable">The OCHA describes the suffering and destruction in Syria as being "unparalleled". Many parties to the conflict have committed violations of international and humanitarian law, and civilians have been impacted gravely. Over half of the population of Syria has been displaced – often multiple times – and an estimated 13.1 million people require humanitarian assistance, of whom 3 million are trapped in besieged and inaccessible-to-humanitarian-actors areas. Syria is ranked 141st in the Human Development Index (2015).</p>
                    </div>
                </div>
            </div>
            <div class="col-md-1 col-2"></div>
        </div>
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-2 col-2"></div>
            <div class="col-md-5 col-8 art-style-back-red">
                <div class="row art-container-country">
                    <p class="text-uppercase art-country-title-style art-unselectable">Articles:</p>
                </div>
                <div class="row">
                    <div class="col-2 art-number-style art-unselectable">1.</div>
                    <div class="col-10 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-2 art-number-style art-unselectable">2.</div>
                    <div class="col-10 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-2 art-number-style art-unselectable">3.</div>
                    <div class="col-10 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-2 art-number-style art-unselectable">4.</div>
                    <div class="col-10 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-2 art-number-style art-unselectable">5.</div>
                    <div class="col-10 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                </div>
            </div>
            <div class="col-md-5 col-2"></div>
        </div>
        <div class="row art-style-20-height"></div>
    </div>
</body>
</html>