import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):

    ###############
    ## SOLUTIONS ##
    ###############

    def best_seam(self):
        height, width = self.height, self.width
        dp = [[(0, None)] * width for _ in range(height+1)]
        for j in range(height+1):
            for i in range(width):
                dp[j][i] = self._pixel_min_energy(i, j, width, height, dp)
        return self._best_seam(height, dp)
    
    def _pixel_min_energy(self, i, j, width, height, dp):
        if j == 0:
            return (self.energy(i, j), None)
        if j == height:
            return (dp[j-1][i][0], i)
        if i == 0:
            adj_rows = [i, i+1]
        elif i == width - 1:
            adj_rows = [i-1, i]
        else:
            adj_rows = [i-1, i, i+1]
        return min((self.energy(i, j) + dp[j-1][r][0], r) for r in adj_rows)
    
    def _best_seam(self, height, dp):
        i = min(dp[height])[1]
        seam = []
        for j in range(height-1, -1, -1):
            seam.append((i, j))
            i = dp[j][i][1]
        seam.reverse()
        return seam

    #########
    ## END ##
    #########

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
