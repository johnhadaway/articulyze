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
    $sql = 'SELECT DISTINCT * FROM burundi WHERE days_in_db > (SELECT MAX(days_in_db) FROM burundi) - 7 ORDER BY score DESC';
    $result = $db->query($sql);
    $rowarray = $result->fetchall(PDO::FETCH_ASSOC);
    $x = 0;

    function show($rowarray){
        global $x;
        $url = $rowarray[$x]['url'];
        $title = $rowarray[$x]['title'];
        echo "<a href='$url'>$title</a>";
        $x++;
    };

    ?>
</head>
<body>
    <nav class="navbar navbar-expand navbar-dark fixed-top art-style-back-grey">
      <a class="navbar-brand" href="#">LOGO</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#art-navbarCollapse" aria-controls="art-navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="art-navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="../index.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../other-pages/about.html">About</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container-fluid">
        <div class="row art-style-20-height"></div>
        <div class="row">
            <div class="col-md-6"></div>
            <div class="col-md-5 art-style-back-red">
                <div class="row">
                    Summary
                </div>
                <div>
                    Text
                </div>
            </div>
            <div class="col-md-1"></div>
        </div>
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-2 col-1"></div>
            <div class="col-md-5 col-5 art-style-back-green">
                <div class="row">
                    <div class="col-4">1</div>
                    <div class="col-8">
                        <?php
                            show($rowarray);
                        ?>
                    </div>
                </div>
                <div class="row">
                    <div class="col-4">2</div>
                    <div class="col-8">
                        <?php
                            show($rowarray);
                        ?>
                    </div>
                </div>
                <div class="row">
                    <div class="col-4">3</div>
                    <div class="col-8">
                        <?php
                            show($rowarray);
                        ?>
                    </div>
                </div>
                <div class="row">
                    <div class="col-4">4</div>
                    <div class="col-8">
                        <?php
                            show($rowarray);
                        ?>
                    </div>
                </div>
                <div class="row">
                    <div class="col-4">5</div>
                    <div class="col-8">
                        <?php
                            show($rowarray);
                        ?>
                    </div>
                </div>
            </div>
            <div class="col-md-5 col-6"></div>
        </div>
        <div class="row art-style-20-height"></div>
    </div>
</body>
</html>